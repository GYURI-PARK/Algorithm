var array = [[Int]]()
var answers = Set<Int>()
var count = 0

//상하좌우
let dx = [0, 0, -1, 1]
let dy = [-1, 1, 0, 0]

for _ in 0..<5 {
    let input = readLine()!.split(separator: " ").map { Int($0)! }
    array.append(input)
}

func dfs(_ row: Int, _ col: Int, _ depth: Int, _ number: Int) {
    if depth == 5 {
        answers.insert(number)
        return
    }
    
    for i in 0..<4 {
        let nx = row + dx[i]
        let ny = col + dy[i]
        
        if (0..<5).contains(nx) && (0..<5).contains(ny) {
            dfs(nx, ny, depth+1, number * 10 + array[nx][ny])
        }
    }
}

for row in 0..<5 {
    for col in 0..<5 {
        dfs(row, col, 0, array[row][col])
    }
}

print(answers.count)