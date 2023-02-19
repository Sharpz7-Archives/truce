
#include "Thread.h"
#include "ThreadController.h"
#include <TimerOne.h>

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
		runned();
	}
};

// Now, let's use our new class of Thread
SensorThread analog0 = SensorThread();

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

	// Add the Threads to our ThreadController
	controller.add(&analog0);

	Timer1.initialize(20000);
	Timer1.attachInterrupt(timerCallback);
	Timer1.start();

}

// Should Poll n times
// If over m of them match, then grip
void decisionAlgorithm() {
	int gripCount = 0;
	int relaxedCount = 0;

	for (int i = 0; i < 10; i++)
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

	if (gripCount > 8)
	{
		analog0._lastAction = GRIP;
		// Turn on LED
		digitalWrite(LED_BUILTIN, HIGH);
	}
	else
	{
		analog0._lastAction = RELAXED;
		// Turn on LED
		digitalWrite(LED_BUILTIN, LOW);
	}
}

// Currently, if the value is greater than 200, it will set the state to GRIP
// If the value is less than 200, it will set the state to RELAXED
State classify() {
	Serial.println(analog0.value);
	if (analog0.value > 200)
	{
		return GRIP;
	}
	else
	{
		return RELAXED;
	}
}


void loop(){
	decisionAlgorithm();
}