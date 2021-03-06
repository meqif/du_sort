# du_sort: a short script for sorting `du` output correctly

Don't you hate when you want to quickly check what's using the most space in
your laptop's disk or server's RAID but `du -hsc *` gives you unsorted output?

Using `du -hsc * | sort --numeric-sort` doesn't help because the units after the
size mess everything up and using `du -k` to display the size in blocks would
allow easy sorting but defeat the purpose of having human-readable units.

So I did what any respectable programmer would do: create a script that would
sort the results exactly as I want them. That's how this script was born.

I hope it's as useful to you as it has been to me. :)

## Testing

Run the tests with `nosetest` (you need to have `nose` installed).
