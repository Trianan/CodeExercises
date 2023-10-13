use std::fs::read_to_string;


fn get_sorted_data(filepath: &str) -> Vec<u32> {
    let data: String = read_to_string(filepath).expect("Unable to read file!");
    let mut data_vec: Vec<u32> = data.lines().map(|n| n.parse().unwrap()).collect();
    data_vec.sort();
    println!("{:?}", &data_vec);
    data_vec
}


fn get_addends(n_vec: &Vec<u32>, target_sum: &u32) -> Option<(u32, u32)> {
    let mut lesser: Vec<u32> = vec![];
    let mut greater: Vec<u32> = vec![]; // No two of these can be addends of target_sum.
    for &n in n_vec {
        if n <= target_sum / 2 {
            lesser.push(n)
        }
        else {
            greater.push(n)
        }
    }
    for n_lesser in &lesser {
        for n_greater in &greater {
            if n_lesser + n_greater == *target_sum {
                return Some((*n_lesser, *n_greater));
            }
        }
    }
    return None;
}


fn get_triple_addends(n_vec: &Vec<u32>, target_sum: &u32) -> Option<(u32, u32, u32)> {
    let mut lower_3rd: Vec<u32> = vec![]; // These will only sum with higher_3rds.
    let mut mid_3rd: Vec<u32> = vec![]; // These will only sum with themselves.
    let mut higher_3rd: Vec<u32> = vec![];
    let lower_3rd_max: u32 = target_sum * 1/3;
    let mid_3rd_max: u32 = target_sum * 2/3;
    let half_target_sum: u32 = target_sum / 2;
    println!("{}, {}", &lower_3rd_max, &mid_3rd_max);

    for n in n_vec {
        if n < &lower_3rd_max {
            lower_3rd.push(*n);
        }
        else if n < &mid_3rd_max{
            mid_3rd.push(*n);
        }
        else {
            higher_3rd.push(*n);
        }
    }
    




    println!("{:?}\n{:?}\n{:?}", &lower_3rd, &mid_3rd, &higher_3rd);


    return None;
}

fn main() {
    let data_vec: Vec<u32> = get_sorted_data("./input.txt");
    let target_sum: u32 = 2020;

    let (n1, n2): (u32, u32) = get_addends(&data_vec, &target_sum).unwrap();
    println!("Addend 1: {n1}, Addend 2: {n2}");

    let mut sum: u32 = n1 + n2;
    let mut product: u32 = n1 * n2;
    println!("Sum: {}, Product: {}", sum, product);

    let (n3, n4, n5): (u32, u32, u32) = get_triple_addends(&data_vec, &target_sum).unwrap();
    println!("Addend 1: {n3}, Addend 2: {n4}, Addend 3: {n5}");

    sum = n3 + n4 + n5;
    product = n3 * n4 * n5;
    println!("Sum: {}, Product: {}", sum, product);
}
