//
//  main.swift
//  Algorithm
//
//  Created by GYURI PARK on 2023/11/28.
//

import Foundation

let n = Int(readLine()!)!
let num = Array(readLine()!.split(separator: " ").map{Int($0)!})
var ans = [Int]()
// var ans = Array(repeating: -1, count: n)
var stack = [Int]()
stack.append(0)

for _ in 0..<n {
    ans.append(-1)
}

for i in 1..<n {
    while !stack.isEmpty && num[stack.last!] < num[i] {
        ans[stack.popLast()!] = num[i]
    }
    stack.append(i)
}

print(ans.map{String($0)}.joined(separator: " "))
