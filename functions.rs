fn main() {                            //Call functions within main function.
    sum();
    subtraction();
    printy_mac_print_print("Sandwiches".to_string());
}

fn sum() {
    let number1: i32 = 7;
    let number2: i32 = 12;
    let result = number1 + number2;
    println!("Your number is {}", result);
    }
    
fn subtraction() {
    let num1: i32 = 5;
    let num2: i32 = 5;
    let result = num1 - num2;
    println!("The result of subtraction is {}", result);
    }

fn printy_mac_print_print(input: String) {
    println!("{}", input);
    }
