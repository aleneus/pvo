package main

import (
	"fmt"
)

// Student represents student
type Student struct {
}

// NewStudent creates new Student and returns pointer to it
func NewStudent() (s *Student, err error) {
	s = new(Student)
	return s, s.Init()
}

// Init Student
func (s *Student) Init() (err error) {
	return nil
}

// Call calls student to the desk
func (s *Student) Call() {
	fmt.Println("It's me")
}

// PoliteStudent represents decorator for Student
type PoliteStudent struct {
	s *Student
}

// NewPoliteStudent creates new PoliteStudent and returns pointer to it
func NewPoliteStudent() (d *PoliteStudent, err error) {
	d = new(PoliteStudent)
	return d, d.Init()
}

// Init PoliteStudent
func (d *PoliteStudent) Init() (err error) {
	d.s, err = NewStudent()
	return err
}

// Call calls politely student to the desk
func (d *PoliteStudent) Call() {
	fmt.Print("Hello! ")
	d.s.Call()
}

func main() {
	student, err := NewPoliteStudent()
	if err != nil {
		panic(err)
	}

	student.Call()
}
