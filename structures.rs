struct Person {  //Struct to hold Perosn data.
  name: String,
  age: u8,
}

struct Point {  //Co-ordinates struct.
  x: f32,
  y: f32,
}

struct Unit; //Placeholder struct for traits with no data. 

struct Pair_or_Tuple(f32, i32)

struct sandwichFilling {
  meat: String;
  sauce: String;
  butter: bool,
}

// Data Analysis
// Scalar types
let x = 5;     // i32
let y = 10.5;   // f64

// Compound types
let tup = (1, "Hello", 1.5); // Tuple
let arr = [1, 2, 3];        // Array

// Collections
let mut vec = Vec::new();   // Vector 
vec.push(1);
vec.push(2);

let mut map = HashMap::new(); // Hashmap
map.insert("key", 1);

//Reading in CSV data.
extern crate csv;

fn main() {
  let mut rdr = csv::Reader::from_reader(io::stdin());
  for record in rdr.records() {
      // Use record
  }

//Reading in JSON
}

extern crate serde;
extern crate serde_json;

use serde_json::Value;

fn main() {
  let json_str = r#"{ "name": "John Doe" }"#;
  let v: Value = serde_json::from_str(json_str);

  println!("{}", v["name"]);  
}

//SQL 
extern crate rusqlite;

use rusqlite::Connection;

fn main() {
  let conn = Connection::open("test.db").unwrap();

  conn.execute(
    "CREATE TABLE person (
                name  TEXT, 
                age INTEGER            
             )", 
    []);
}

//Plotting
extern crate plotters;

use plotters::prelude::*;

fn main() {
  let mut data = Vec::new();
  data.push((1., 2.));
  data.push((2., 3.));
  data.push((3., 1.));

  let mut chart = ChartBuilder::on(&data)
                            .caption("Example plot", ("sans-serif", 50))
                            .set_label_area_size(LabelAreaPosition::Left, 40)  
                            .line_chart();

  chart.configure_mesh()  
     .draw()
     .unwrap(); 
}

//Logistic regression using rustlearn.
extern crate rustlearn;
use rustlearn::{Dataset, LogisticRegression, Metric};

fn main() {
  let mut dataset = Dataset::new();
  dataset.push([-1., -2.], -1);
  dataset.push([0., 1.], 1);
  dataset.push([2., 1.], 1);

  let mut lr = LogisticRegression::default();
  lr.fit(&dataset, Metric::Accuracy);

  let pred = lr.predict(&[-1., -2.]);
  assert_eq!(pred, -1);

  let pred = lr.predict(&[1., 2.]);
  assert_eq!(pred, 1);  
}

//Closer look at rustlearn crate for Machine Learning. 
//Models
//logistic regression using stochastic gradient descent,
//support vector machines using the libsvm library,
//decision trees using the CART algorithm,
//random forests using CART decision trees, and
//factorization machines.

////Basic Objects
Affine schemes
Varieties (algebraic varieties)
Polynomial rings and their ideals
Affine algebraic sets
Projective schemes
Morphisms of schemes
Intermediate Objects
Sheaves (of modules, functions)
Line bundles and vector bundles (locally free sheaves)
Divisors and linear systems
Cohomology groups (sheaf cohomology)
Blow-ups and birational maps
Chow groups and intersection theory
Advanced Objects
Picard schemes and Albanese varieties
Moduli spaces (e.g., moduli of curves, vector bundles)
Derived schemes and derived stacks
Stacks (Deligne-Mumford stacks, Artin stacks)
Hom schemes and Hilbert schemes
Complex analytic spaces (generalizations involving complex structures)
Highly Sophisticated / Modern Objects
Derived algebraic geometry objects (derived schemes, derived stacks)
Higher stacks and ∞\infty∞-categories
Spectral schemes and spectral algebraic geometry
Motivic cohomology and motives
Noncommutative algebraic geometry objects (noncommutative schemes, dg-categories)
Brane stacks and derived categories in string theory///
