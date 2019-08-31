/*
sort function object
*/

#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

class Student
{
public:
	string name;
	int score;
	Student(string name, int score) {
		this->name = name;
		this->score = score;
	}

	bool operator <(Student &student) {
		return this->score < student.score;
	}
};


int main(void) {
	Student students[] = {
		Student("kim",99),
		Student("park",90),
		Student("lee",95)
	};

	sort(students, students + 3);

	for (int i = 0; i < 3; i++)
	{
		cout << students[i].name << endl;
	}
	return 0;
}

