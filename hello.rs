fn main() {
    println!("Hello World!");  // Print text to the console.
}

// Collatz Conjecture Algorithm
fn collatz_conjecture(start_number: u64, max_steps: u64) -> Option<u64> { // -> Option means our function can return some value or None.
    let mut current_number = start_number;    // mut stands for mutable, meaning that current_number and step_count are variable. All let objects are immutable by default. 
    let mut step_count = 0;

    while current_number != 1 && step_count < max_steps {
        if current_number % 2 == 0 {
            current_number /= 2;
        } else {
            current_number = current_number * 3 + 1;
        }
        step_count += 1;
    }

    if current_number == 1 {
        Some(step_count) // Returns the number of steps to reach 1. 'Some' and 'None' are used in Rust to bypass NULL pointers. 
    } else {
        None // Returns None if the maximum steps is reached without reaching 1
    }
}

// Example Case:
fn main() {
    let start_number = 6;
    let max_steps = 10;
    let result = collatz_conjecture(start_number, max_steps);

    match result {    // match function maps result in this case to either of the two options below. => is equivalent of IF THEN statement.
        Some(steps) => println!("It took {} steps to reach 1", steps),
        None => println!("Reached max steps without reaching 1"),
    }
}
