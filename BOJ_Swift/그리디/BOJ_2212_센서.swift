let n = Int(readLine()!)!
let k = Int(readLine()!)!

var sensor = readLine()!.split(separator: " ").compactMap { Int($0)! }
sensor.sort()

var li = [Int]()

for i in 0..<n-1 {
    li.append(sensor[i+1] - sensor[i])
}

var res = 0
li.sort()

if n > k {
    for i in 0..<n-k {
        res += li[i]
    }
}

print(res)