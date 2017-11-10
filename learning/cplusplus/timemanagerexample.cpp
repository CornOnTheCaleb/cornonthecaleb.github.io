#include <iostream>
#include <unistd.h> // Included for sleep()
#include "timemanager.h"

using namespace std;

int main (int argc, char ** argv)
{
  TimeManager time;
  cout << "Runtime: " << time.get_runtime() << " seconds." << endl;
  sleep(1); // Pause execution for 1 second
  cout << "Runtime: " << time.get_runtime() << " seconds." << endl;
  time.update();
  sleep(2);
  time.update();
  cout << "Delta time: " << time.get_delta_time() << " seconds." << endl;
  return 0;
}
