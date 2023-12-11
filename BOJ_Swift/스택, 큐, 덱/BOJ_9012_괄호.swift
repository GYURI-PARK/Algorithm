// 1.

let n = Int(readLine()!)!

for _ in 0..<n {
    let input = readLine()!
    var result = 0
    for i in input {
        if String(i) == "(" {
            result += 1
        }
        if String(i) == ")" {
            result -= 1
        }
        if result == -1 {
            break
        }
    }
    if result == 0 {
        print("YES")
    } else {
        print("NO")
    }
}

// 2.
// 안쪽 반복문(for문)에 break를 걸어주면 해당 반복문은 종료되고 밖의 for문은 여전히 실행된다.

import Foundation

let n = Int(readLine()!)!

for _ in 0..<n {
    var stack = [String]()
    var isFalse = false
    let order = readLine()!

    for i in order {
        if (i == "(") {
            stack.append("(")
        } else {
            if stack.isEmpty {
                isFalse = true
                break
            } else {
                stack.removeLast()
            }
        }
    }
    
    if stack.isEmpty && !isFalse {
        print("YES")
    } else {
        print("NO")
    }
}