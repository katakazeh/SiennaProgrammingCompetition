def main():
    # Your code for Problem 6 goes here,
    # press the >Run button to execute

  p = int(input())
  n = int(input())
  routes = []
  for _ in range(n):
    _ = int(input())
    routes.append([int(i) for i in input().split()])

  graph = {station: [] for station in range(1, p + 1)}
  for route in routes:
    for i in range(len(route) - 1):
      graph[route[i]].append(route[i + 1])
  
  def dfs(source, target, num_paths):
    # print(source)
    n_paths = 0
    if source == target:
      return n_paths + 1
    for neighbor in graph[source]:
      n_paths += dfs(neighbor, target, n_paths)
    return n_paths
  print(dfs(1, p, 0))
  
    
# Include a call to your main function.
main()
