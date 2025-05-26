tell application "Google Chrome"
    activate
    open location "https://chat.openai.com"
end tell

delay 6

tell application "System Events"
    keystroke "n"
    delay 1
    keystroke "Write an SEO-optimized blog post about the best ergonomic chairs for remote workers. Format in markdown. Include a title and use a casual tone."
    key code 36 -- press Return
    delay 30 -- wait for response to generate
    keystroke "a" using {command down}
    keystroke "c" using {command down}
end tell