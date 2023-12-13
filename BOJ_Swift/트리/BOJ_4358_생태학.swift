//
//  main.swift
//  Algorithm
//
//  Created by GYURI PARK on 2023/11/28.
//

import Foundation

var trees = [String: Int]()
var cnt = 0

while let tree = readLine(), !tree.isEmpty {
    cnt += 1
    if let count = trees[tree] {
        trees[tree] = count + 1
    } else {
        trees[tree] = 1
    }
}

var sorts = trees.sorted{$0.0 < $1.0}

for i in sorts {
    let per = (Double(i.value) / Double(cnt) * 100)
    print("\(i.key) \(String(format: "%.4f", per))")
}
