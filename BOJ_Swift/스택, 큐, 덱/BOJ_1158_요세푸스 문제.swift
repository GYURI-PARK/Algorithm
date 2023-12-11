import Foundation

let input = readLine()!.split(separator: " ").map{ Int(String($0))! }
let n = input[0]
let k = input[1]
var count = k-1

var arr = Array(1...n)
var res = [Int]()

while !arr.isEmpty {
    count %= arr.count
    res.append(arr.remove(at: count))
    count += k - 1
}

print("<" + res.map{String($0)}.joined(separator: ", ") + ">")
