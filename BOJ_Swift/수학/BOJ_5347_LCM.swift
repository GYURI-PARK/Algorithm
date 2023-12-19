import Foundation

let n = Int(readLine()!)!

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map({ Int($0)! })
    let a = input[0]
    let b = input[1]
    
    var li1 = [Int]()
    var li2 = [Int]()
    
    for i in 2..<a+1 {
        if (a % i) == 0 {
            li1.append(i)
        }
    }
    
    for j in 2..<b+1 {
        if (b % j) == 0 {
            li2.append(j)
        }
    }
    
    let li = Set(li1).intersection(Set(li2))
    
    if li.isEmpty {
        print(a * b)
    } else {
        let maxone = li.max()!
        print(maxone * (a / maxone) * (b / maxone))
    }
}



// 깔끔하게

import Foundation

// 최대 공약수 구해줌
func LCM(_ a: Int, _ b: Int) -> Int {
    return b % a == 0 ? a : LCM(b % a, a)
}

let n = Int(readLine()!)!

for _ in 0..<n {
    let input = readLine()!.split(separator: " ").map({ Int($0)! })
    print(input[0] * input[1] / LCM(input[0], input[1]))
}
