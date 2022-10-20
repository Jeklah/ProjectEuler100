// projecct euler problem 19
//
// Counting Sundays
// Author: Jeklah
// Status: Solved
//
// You are given the following information, but you may prefer to do some research for yourself.
//
// 1 Jan 1900 was a Monday.
// Thirty days has September,
// April, June and November.
// All the rest have thirty-one,
// Saving February alone,
// Which has twenty-eight, rain or shine.
// And on leap years, twenty-nine.
// A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
// How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

fn main() {
    let mut days = 0;
    let mut sundays = 0;
    for year in 1900..2001 {
        for month in 1..13 {
            if year >= 1901 && days % 7 == 0 {
                sundays += 1;
            }
            days += days_in_month(month, year);
        }
    }
    println!("{}", sundays);
}

fn days_in_month(month: u32, year: u32) -> u32 {
    match month {
        1 | 3 | 5 | 7 | 8 | 10 | 12 => 31,
        4 | 6 | 9 | 11 => 30,
        2 if is_leap_year(year) => 29,
        2 => 28,
        _ => 0,
    }
}

fn is_leap_year(year: u32) -> bool {
    year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)
}

// output
// 171

// time
// real    0m0.006s
// user    0m0.002s
// sys     0m0.002s

// size
// 0m0.010s

// memory
// 0m0.010s

// disk
// 0m0.000s

// notes
// 0m0.002s
