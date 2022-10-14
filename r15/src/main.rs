// project euler problem 15
// Lattice paths
//
// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
// How many such routes are there through a 20×20 grid?
// https://projecteuler.net/problem=15
//
//
//
//
//

fn main() {
    let mut grid: Vec<Vec<u64>> = vec![vec![0; 21]; 21];

    for x in 0..21 {
        grid[x][20] = 1;
        grid[20][x] = 1;
    }

    for x in (0..20).rev() {
        for y in (0..20).rev() {
            grid[x][y] = grid[x + 1][y] + grid[x][y + 1];
        }
    }
    println!("Number of routes: {}", grid[0][0]);
}

// This is the end of the file.
