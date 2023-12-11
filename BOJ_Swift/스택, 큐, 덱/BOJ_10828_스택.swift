import Foundation

let n = Int(readLine()!)!
var stack = [Int]()

for _ in 0..<n {
    let order = readLine()!.split(separator: " ")
    if (order[0] == "push") {
        stack.append(Int(order[1])!)
    } else if (order[0] == "pop") {
        if stack.isEmpty {
            print("-1")
        } else {
            print(stack.popLast()!)
        }
    } else if (order[0] == "size") {
        print(stack.count)
    } else  if (order[0] == "empty") {
        if stack.isEmpty {
            print("1")
        } else {
            print("0")
        }
    } else if (order[0] == "top") {
        if stack.isEmpty {
            print("-1")
        } else {
            print(stack.last!)
        }
    }
}
