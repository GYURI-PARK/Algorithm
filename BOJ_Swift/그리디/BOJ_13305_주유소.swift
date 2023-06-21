import Foundation

func calculateMinCost() -> Int {
    let n = Int(readLine()!)!
    let distance = readLine()!.split(separator: " ").map { Int($0)! }
    let price = readLine()!.split(separator: " ").map { Int($0)! }

    var res = distance[0] * price[0]
    var cheapest = price[0]

    for i in 1..<n-1 {
        if cheapest > price[i] {
            cheapest = price[i]
        }

        res += cheapest * distance[i]
    }

    return res
}

print(calculateMinCost())
