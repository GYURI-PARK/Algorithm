import Foundation

let n = Int(readLine()!)!
var data = Array(readLine()!.split(separator: " ").enumerated()).map { ($0, Int($1)!) }
var idx = 0

while !data.isEmpty {
    let tmp = data.remove(at: idx)
    print(tmp.0 + 1, terminator: " ")

    if tmp.1 < 0 && !data.isEmpty {
        idx = (idx + tmp.1) % data.count
        if idx < 0 {
            idx += data.count
        }
    } else if tmp.1 > 0 && !data.isEmpty {
        idx = (idx + (tmp.1 - 1)) % data.count
    }
}
