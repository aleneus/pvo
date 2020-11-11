// package main presents command pattern example in golang
package main

import (
	"fmt"
)

// Score represents some score to be managed
type Score struct {
	amount int
}

// NewScore creates new Score and returns pointer to it
func NewScore() (s *Score) {
	s = new(Score)
	s.amount = 0
	return s
}

// Inc adds 1 to amount
func (s *Score) Inc() {
	s.amount++
}

// Dec subs 1 from amount
func (s *Score) Dec() {
	s.amount--
}

// String represents the score as string
func (s Score) String() string {
	return fmt.Sprint(s.amount)
}

//
// Command interface

// Command is the 'command' in the pattern
type Command interface {
	// Do executes command
	Do()
}

//
// Concrete commands

// CommandInc represents command for incriminating the score
type CommandInc struct {
	score *Score
}

// NewCommandInc creates new CommandInc and returns pointer to it
func NewCommandInc(score *Score) (c *CommandInc) {
	c = new(CommandInc)
	c.score = score
	return c
}

// Do executes command
func (c *CommandInc) Do() {
	c.score.Inc()
}

// CommandDec represents command for decrement the score
type CommandDec struct {
	score *Score
}

// NewCommandDec creates new CommandDec and returns pointer to it
func NewCommandDec(score *Score) (c *CommandDec) {
	c = new(CommandDec)
	c.score = score
	return c
}

// Do executes command
func (c *CommandDec) Do() {
	c.score.Dec()
}

//
// Who will collect and send commands?

// Invoker represents the sender of commands
type Invoker struct {
	commands []Command
}

// NewInvoker creates new Invoker and returns pointer to it
func NewInvoker() (inv *Invoker) {
	inv = new(Invoker)
	return inv
}

// Store stores command to be executed in future
func (inv *Invoker) Store(c Command) {
	inv.commands = append(inv.commands, c)
}

// Execute executes all stored commands
func (inv *Invoker) Execute() {
	// NOTE: stubby implementation
	for _, c := range inv.commands {
		c.Do()
	}
	inv.commands = make([]Command, 0)
}

//
// Demo

func main() {
	s := NewScore()
	i := NewInvoker()

	i.Store(NewCommandInc(s))
	i.Store(NewCommandInc(s))
	i.Store(NewCommandDec(s))

	i.Execute()

	fmt.Println(s)
}
