from chardet.universaldetector import UniversalDetector

with open(file_path, 'rb') as f:  
  detector = UniversalDetector()
  for line in f:
    detector.feed(line)
    if detector.done:
      break
  detector.close()
  result = detector.result
