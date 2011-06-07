#!/usr/bin/env ruby

INPUT_FILE = STDIN

input = INPUT_FILE.readlines

ordered_data = input.sort_by do |line|
  size = line.split.first

  case size[-1]
  when "K"
    size = size.to_f
  when "M"
    size = size.to_f * 1024
  when "G"
    size = size.to_f * 1024**2
  else # size given in blocks, don't mess with it
    size = size.to_f
  end
end

puts ordered_data
