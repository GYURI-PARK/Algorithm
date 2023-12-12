//
//  main.swift
//  Algorithm
//
//  Created by GYURI PARK on 2023/11/28.
//

import Foundation

let input = Array(readLine()!)
var stack = [Int]()
var ans = [String]()
var indices = [(Int, Int)]()

for i in 0..<input.count {
    if input[i] == "(" {
        stack.append(i)
    } else if input[i] == ")" {
        indices.append((stack.popLast()!, i))
    }
}

for i in 0..<indices.count {
    for comb in indices.combinations(ofCount: i + 1) {
        var temp = input
        for idx in comb {
            temp[idx.0] = " "
            temp[idx.1] = " "
        }
        let result = temp.filter { $0 != " " }.map { String($0) }.joined()
        if result != String(input) {
            ans.append(result)
        }
    }
}

let uniqueAns = Set(ans)
let sortedUniqueAns = uniqueAns.sorted()

for i in sortedUniqueAns {
    print(i)
}

extension Array {
    func combinations(ofCount count: Int) -> [[Element]] {
        guard count > 0 else { return [[]] }
        guard let first = first else { return [] }

        let withoutFirst = Array(self[1...])
        let combinationsWithoutFirst = withoutFirst.combinations(ofCount: count - 1)
        let combinationsWithFirst = combinationsWithoutFirst.map { [first] + $0 }

        return combinationsWithoutFirst + combinationsWithFirst
    }
}
