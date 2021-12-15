use std::env;
use std::fs;
use std::collections::VecDeque;
use std::iter::FromIterator;
use std::str::FromStr;

fn main() {
    let args: Vec<String> = env::args().collect();
    let filename = &args[1];

    println!("In file {}", filename);

    let contents = fs::read_to_string(filename)
        .expect("Something went wrong reading the file");

    let mut depth_readings = VecDeque::from_iter(contents.split("\n"));

    let prev_reading_str = depth_readings.pop_front().unwrap();
    let mut prev_reading = i32::from_str(prev_reading_str).unwrap();

    let mut depth_increases = 0;
    for cur_reading_str in depth_readings {
        let cur_reading = i32::from_str(cur_reading_str).unwrap();

        println!("comparing {} {}", prev_reading, cur_reading);
        if prev_reading < cur_reading {
            depth_increases += 1;
        }

        prev_reading = cur_reading;
    }

    println!("Number of depth increases: {}", depth_increases)
}