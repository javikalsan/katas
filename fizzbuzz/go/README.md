# FizzBuzz kata

The classic [FizzBuzz kata](https://codingdojo.org/kata/FizzBuzz/)

```
❯ go test -v
=== RUN   TestSpec

  Given some integer with a starting value
    when the integer is divisible by 3
      the result should be 'Fizz' ✔
    when the integer is divisible by 5
      the result should be 'Buzz' ✔
    when the integer is divisible by 3 and 5
      the result should be 'FizzBuzz' ✔
    when the integer is not divisible by 3 or 5
      the result should be the integer itself ✔


4 total assertions
```
