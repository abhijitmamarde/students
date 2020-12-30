sample_students = [
  ["aaa", 123],
  ["bbb", 125],
  ["ccc", 124]
]

"""
TODO 3. read the students records as in above format from the json file: "students.json"
"""

def get_toppers(students, how_many=1):
  """
  Get the topper students

  TODO: 1. Replace this function body and implement the actual logic
  """
  if how_many == 1:
    return ["bbb"]
  if how_many == 2:
    return ["bbb", "ccc"]
  if how_many >= 3:
    return ["bbb", "ccc", "aaa"]

"""
TODO: 2. all below asserts should work!
"""
assert get_toppers(sample_students, how_many=1) == ["bbb"]
assert get_toppers(sample_students, how_many=2) == ["bbb", "ccc"]
assert get_toppers(sample_students, how_many=3) == ["bbb", "ccc", "aaa"]
assert get_toppers(sample_students, how_many=4) == ["bbb", "ccc", "aaa"]

print("PASS")
