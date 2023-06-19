import Foundation

let input = readLine()!.split(separator: " ").map { Int($0)! }
let n = input[0]
let m = input[1]

let li = readLine()!.split(separator: " ").map { Int($0)! }

var start = 0
var end = li.max()! * m
var res = 0

while start <= end {
    let mid = (start + end) / 2
    if li.map { mid / $0 }.reduce(0, +) >= m {
        res = mid
        end = mid - 1
    } else {
        start = mid + 1
    }
}

print(res)
