
#include "Thread.h"
#include "ThreadController.h"

// Constants
#define POLL_COUNT 10000
#define ACCEPTABLE_ERROR 0.01

// Number between 0 and 1023
#define THRESHOLD 150

// create enum
enum State {
    GRIP,
    RELAXED,
};

// Create a new Class, called SensorThread, that inherits from Thread
class SensorThread: public Thread
{
public:
    int value;
    int pin;
    State _lastAction;

    // No, "run" cannot be anything...
    // Because Thread uses the method "run" to run threads,
    // we MUST overload this method here. using anything other
    // than "run" will not work properly...
    void run(){
        // Reads the analog pin, and saves it localy
        value = analogRead(pin);
        Serial.println(value);
        runned();
    }
};

// Now, let's use our new class of Thread
SensorThread analog0 = SensorThread();

Thread outputThread = Thread();

// Instantiate a new ThreadController
ThreadController controller = ThreadController();

// This is the callback for the Timer
void timerCallback(){
    controller.run();
}

void setup(){

    Serial.begin(9600);

    // Configures Thread analog0
    analog0.pin = A0;
    analog0.setInterval(100);

    outputThread.onRun(setOutput);
    outputThread.setInterval(1000);


    // Add the Threads to our ThreadController
    controller.add(&analog0);
    controller.add(&outputThread);

    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
}

// Should Poll POLL_COUNT times
// If over (POLL_COUNT - (POLL_COUNT * ACCEPTABLE_ERROR)) of them match
// Then do that action
void decisionAlgorithm() {
    int gripCount = 0;
    int relaxedCount = 0;

    for (int i = 0; i < POLL_COUNT; i++)
    {
        switch (classify())
        {
            case GRIP:
                gripCount++;
                break;
            case RELAXED:
                relaxedCount++;
                break;
        }

    }

    if (gripCount > POLL_COUNT - (POLL_COUNT * ACCEPTABLE_ERROR))
    {
        analog0._lastAction = GRIP;
        // Turn on LED
        digitalWrite(LED_BUILTIN, HIGH);
    }
    if (relaxedCount > POLL_COUNT - (POLL_COUNT * ACCEPTABLE_ERROR))
    {
        analog0._lastAction = RELAXED;
        // Turn on LED
        digitalWrite(LED_BUILTIN, LOW);
    }
}

// Currently, if the value is greater than THRESHOLD, it will set the state to GRIP
// If the value is less than THRESHOLD, it will set the state to RELAXED
State classify() {
    timerCallback();

    if (analog0.value > THRESHOLD)
    {
        return GRIP;
    }
    else
    {
        return RELAXED;
    }
}

// Use the first 3 digital pints to encode 8 state.
// Only the first 2 states are used: GRIP and RELAXED
void setOutput() {
    int state = analog0._lastAction;

    if (state == RELAXED) {
        write(LOW, LOW, HIGH);
    } else if (state == GRIP) {
        write(LOW, HIGH, LOW);
    } else {
        write(LOW, LOW, LOW);
    }

}

// write function that will take the three pins and set them to the correct state
void write(int pin2, int pin3, int pin4) {
    digitalWrite(2, pin2);
    digitalWrite(3, pin3);
    digitalWrite(4, pin4);
}


void loop(){
    decisionAlgorithm();
}