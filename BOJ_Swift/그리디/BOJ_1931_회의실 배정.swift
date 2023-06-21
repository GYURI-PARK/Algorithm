import Foundation

func calculateMinStops() -> Int {
    let n = Int(readLine()!)!
    var li = [[Int]]()
    var res = 1
    
    for _ in 0..<n {
        li.append(readLine()!.split(separator: " ").map { Int($0)! })
    }
    
    let sortedList = li.sorted { $0[1] < $1[1] || ($0[1] == $1[1] && $0[0] < $1[0]) }
    
    var endTime = sortedList[0][1]
    
    for i in 1..<n {
        if sortedList[i][0] >= endTime {
            endTime = sortedList[i][1]
            res += 1
        }
    }
    
    return res
}

print(calculateMinStops())
