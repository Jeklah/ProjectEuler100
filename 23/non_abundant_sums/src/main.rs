// project euler problem 23
// https://projecteuler.net/problem=23
// Author: Jeklah
//
// This is a solution to the problem 23 of project euler.
//

fn main() {
    let mut abundant_numbers = Vec::new();
    for i in 1..28123 {
        if is_abundant(i) {
            abundant_numbers.push(i);
        }
    }
    let mut sum = 0;
    for i in 1..28123 {
        if !is_sum_of_two_abundant_numbers(i, &abundant_numbers) {
            sum += i;
        }
    }
    println!("{}", sum);
}

fn is_abundant(n: u32) -> bool {
    let mut sum = 0;
    for i in 1..n {
        if n % i == 0 {
            sum += i;
        }
    }
    sum > n
}

fn is_sum_of_two_abundant_numbers(n: u32, abundant_numbers: &Vec<u32>) -> bool {
    for i in abundant_numbers {
        if i > &n {
            return false;
        }
        for j in abundant_numbers {
            if i + j == n {
                return true;
            }
        }
    }
    false
}
