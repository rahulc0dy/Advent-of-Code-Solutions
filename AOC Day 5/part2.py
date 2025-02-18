'''
--- Part Two ---
While the Elves get to work printing the correctly-ordered updates, you have a little time to fix the rest of them.

For each of the incorrectly-ordered updates, use the page ordering rules to put the page numbers in the right order. For the above example, here are the three incorrectly-ordered updates and their correct orderings:

75,97,47,61,53 becomes 97,75,47,61,53.
61,13,29 becomes 61,29,13.
97,13,75,29,47 becomes 97,75,47,29,13.
After taking only the incorrectly-ordered updates and ordering them correctly, their middle page numbers are 47, 29, and 47. Adding these together produces 123.

Find the updates which are not in the correct order. What do you get if you add up the middle page numbers after correctly ordering just those updates?
'''
from collections import defaultdict, deque

def parse_input(input_text):
    sections = input_text.strip().split("\n\n")
    rules = [tuple(map(int, line.split('|'))) for line in sections[0].split('\n')]
    updates = [list(map(int, line.split(','))) for line in sections[1].split('\n')]
    return rules, updates

def is_valid_ordering(update, rules):
    position = {page: i for i, page in enumerate(update)}
    
    for before, after in rules:
        if before in position and after in position:
            if position[before] > position[after]:
                return False 
    
    return True

def find_middle_page(update):
    return update[len(update) // 2] 

def build_dependency_graph(rules, pages):
    graph = defaultdict(set)
    in_degree = {page: 0 for page in pages}
    for before, after in rules:
        if before in pages and after in pages:
            graph[before].add(after)
            in_degree[after] += 1
    return graph, in_degree

def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    sorted_order = []
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return sorted_order

def fix_order(update, rules):
    graph, in_degree = build_dependency_graph(rules, set(update))
    return topological_sort(graph, in_degree)

def sum_of_middle_pages_after_fixing(input_text):
    rules, updates = parse_input(input_text)
    invalid_updates = [update for update in updates if not is_valid_ordering(update, rules)]

    fixed_updates = [fix_order(update, rules) for update in invalid_updates]
    return sum(find_middle_page(update) for update in fixed_updates)

with open("input.txt","r") as file:
    input_text = file.read()

print(sum_of_middle_pages_after_fixing(input_text))