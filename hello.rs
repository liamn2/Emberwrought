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

// Macros in std crate. '::' is the path seperator in Rust. Pythonically, it would be '.', as in matplotlib.pyplot.  
fn stdmacros() {
    arch::is_aarch64_feature_detected();        
    arch::is_arm_feature_detected();
    arch::is_loongarch_feature_detected();
    arch::is_mips64_feature_detected();
    arch::is_mips_feature_detected();
    arch::is_powerpc64_feature_detected();
    arch::is_powerpc_feature_detected();
    arch::is_riscv_feature_detected();
    arch::is_s390x_feature_detected();
    arch::is_x86_feature_detected();            // All macros above and including this line are checks for enabled features                                                    of respective CPU architectures. 
    assert;                                   // Asserts that a boolean expression is true at runtime.
    assert_eq;
    assert_matches::assert_matches;
    assert_matches::debug_assert_matches;
    assert_ne;
    cfg;
    cfg_match;
    column;
    compile_error;
    concat;
    concat_bytes;
    concat_idents;
    const_format_args;
    dbg;
    debug_assert;
    debug_assert_eq;
    debug_assert_ne;
    env;
    eprint;
    eprintln;
    file;
    format;
    format_args;
    format_args_nl;
    future::join;
    include;
    include_bytes;
    include_str;
    intrinsics::mir::mir;
    intrinsics::mir::place;
    io::const_error;
    is_x86_feature_detected;
    line;
    log_syntax;
    matches;
    mem::offset_of;
    module_path;
    option_env;
    panic;
    pat::pattern_type;
    pin::pin;
    prelude::v1::deref;
    prelude::v1::type_ascribe;
    print;
    println;
    ptr::addr_of;
    ptr::addr_of_mut;
    simd::prelude::simd_swizzle;
    simd::simd_swizzle;
    stringify;
    task::ready;
    thread_local;
    todo;
    trace_macros;
    try;
    unimplemented;
    unreachable;
    unsafe_binder::unwrap_binder;
    unsafe_binder::wrap_binder;
    vec;
    write;
    writeln;
}

fn rustKeywords() {
    SelfTy //The implementing type within a trait or impl block, or the current type within a type definition.
    as //Cast between types, or rename an import.
    async //Returns a Future instead of blocking the current thread.
    await //Suspend execution until the result of a Future is ready.
    break //Exit early from a loop or labelled block.
    const //Compile-time constants, compile-time evaluable functions, and raw pointers.
    continue //Skip to the next iteration of a loop.
    crate //A Rust binary or library.
    dyn //dyn is a prefix of a trait object’s type.
    else //What expression to evaluate when an if condition evaluates to false.
    enum //A type that can be any one of several variants.
    extern //Link to or import external code.
    false //A value of type bool representing logical false.
    fn //A function or function pointer.
    for //Iteration with in, trait implementation with impl, or higher-ranked trait bounds (for<'a>).
    if //Evaluate a block if a condition holds.
    impl //Implementations of functionality for a type, or a type implementing some functionality.
    in //Iterate over a series of values with for.
    let //Bind a value to a variable.
    loop //Loop indefinitely.
    match //Control flow based on pattern matching.
    mod //Organize code into modules.
    move //Capture a closure’s environment by value.
    mut //A mutable variable, reference, or pointer.
    pub //Make an item visible to others.
    ref //Bind by reference during pattern matching.
    return //Returns a value from a function.
    self //The receiver of a method, or the current module.
    static //A static item is a value which is valid for the entire duration of your program (a 'static lifetime).
    struct //A type that is composed of other types.
    super //The parent of the current module.
    trait //A common interface for a group of types.
    true //A value of type bool representing logical true.
    type //Define an alias for an existing type.
    union //The Rust equivalent of a C-style union.
    unsafe //Code or interfaces whose memory safety cannot be verified by the type system.
    use //Import or rename items from other crates or modules, use values under ergonomic clones semantic, specify with use<..>.
    where //Add constraints that must be upheld to use an item.
    while //Loop while a condition is upheld.
}
