// PROJECT EULER PROBLEM #1 - Trianan (Started: May 4/2023, Finished: May 4/2023)
const MAX_N: u32 = 1000;
fn main() {
    let mut sum: u32 = 0;
    for n in 1..MAX_N {
        if (n % 3 == 0) && (n % 5 == 0) {
            sum += n;
        }
        else if (n % 3 == 0) || (n % 5 == 0) {
            sum += n;
        }
    }
    println!("Sum of all multiples of 3 or 5: {}", sum);
}