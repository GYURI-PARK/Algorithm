import Foundation

let n = Int(readLine()!)!
let m = Int(readLine()!)!

var vip = [Int]()

for _ in 0..<m {
    let vipSeat = Int(readLine()!)!
    vip.append(vipSeat)
}

var dp = [Int](repeating: 0, count: n+1)
dp[0] = 1
dp[1] = 1

if n >= 2 {
    dp[2] = 2
    for i in 3..<n+1 {
        dp[i] = dp[i-1] + dp[i-2]
    }
}

var res = 1
if m > 0 {
    var tmp = 0
    for j in 0..<m {
        res *= dp[vip[j] - 1 - tmp]
        tmp = vip[j]
    }
    res *= dp[n-tmp]
} else {
    res = dp[n]
}

print(res)