#include <iostream>
#include "vector.h"

using namespace std;

int main (int argc, char ** argv)
{
  Vector<1> vector1D(1.0);
  Vector<2> vector2D(1.0, 2.0);
  Vector<3> vector3D(1.0, 2.0, 3.0);
  cout << "1D Vector: " << vector1D << endl;
  cout << "2D Vector: " << vector2D << endl;
  cout << "3D Vector: " << vector3D << endl;
  return 0;
}
