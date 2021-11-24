package fizzbuzz

import (
	"testing"

	. "github.com/smartystreets/goconvey/convey"
)

func TestSpec(t *testing.T) {
	Convey("Given some integer with a starting value", t, func() {
		Convey("when the integer is divisible by 3", func() {
			Convey("the result should be 'Fizz'", func() {
				So(FizzBuzz(3), ShouldEqual, "Fizz")
			})
		})
		Convey("when the integer is divisible by 5", func() {
			Convey("the result should be 'Buzz'", func() {
				So(FizzBuzz(5), ShouldEqual, "Buzz")
			})
		})
		Convey("when the integer is divisible by 3 and 5", func() {
			Convey("the result should be 'FizzBuzz'", func() {
				So(FizzBuzz(15), ShouldEqual, "FizzBuzz")
			})
		})
		Convey("when the integer is not divisible by 3 or 5", func() {
			Convey("the result should be the integer itself", func() {
				So(FizzBuzz(7), ShouldEqual, "7")
			})
		})
	})
}
