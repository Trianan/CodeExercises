// PROJECT EULER PROBLEM #2 - Trianan (Started: May 4/2023, Finished: May 4/2023)
const MAX_N: u32 = 4000000;
fn main() {
    let mut n1: u32 = 1;
    let mut n2: u32 = 2;
    let mut sum: u32 = 2;
    while n2 < MAX_N {
        let n3 = n1 + n2;
        n1 = n2;
        n2 = n3;
        if n3 % 2 == 0 {
            sum += n3;
        }
    }
    println!("Sum: {}", sum)
}