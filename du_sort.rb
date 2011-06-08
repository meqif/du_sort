#!/usr/bin/env ruby

INPUT_FILE = STDIN

input = INPUT_FILE.readlines

ordered_data = input.sort_by do |line|
  size = line.split.first
  # some locales use commas as decimal separators
  size.sub!(",", ".")

  units = %w{B K M G T P}
  exponents = Hash[units.zip(0..units.length)]

  if exponents.has_key? size[-1]
    size = size.to_f * 1024 ** exponents[size[-1]]
  else # size given in blocks, don't mess with it
    size = size.to_f
  end
end

puts ordered_data
