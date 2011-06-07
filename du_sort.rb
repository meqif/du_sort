#!/usr/bin/env ruby

INPUT_FILE = STDIN

input = INPUT_FILE.readlines

ordered_data = input.sort_by do |line|
  size = line.split.first
  # some locales use commas as decimal separators
  size.sub!(",", ".")

  case size[-1]
  when "B"
    size = size.to_f
  when "K"
    size = size.to_f * 1024
  when "M"
    size = size.to_f * 1024**2
  when "G"
    size = size.to_f * 1024**3
  else # size given in blocks, don't mess with it
    size = size.to_f
  end
end

puts ordered_data
