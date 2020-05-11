from subprocess import Popen, PIPE
from applepyautomator.keycode import COMMON_KEYS


def quit_app(appname, delay=0.125):
    scpt = '''
        on run {input, parameters}
            (* Your script goes here *)
            delay ''' + str(delay) + '''
            tell application "''' + appname + '''"
                quit
            end tell
            return input
        end run'''
    args = ['', '']

    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)
    if p.returncode == 0:
        return p.returncode
    else:
        raise Exception(stderr)


def type_keystroke(text, delay=0.125):
    scpt = '''
        on run {input, parameters}
            -- Type \'''' + text + '''\'
            delay ''' + str(delay) + '''
            set timeoutSeconds to 2.0
            set uiScript to "keystroke \\"''' + text + '''\\""
            my doWithTimeout(uiScript, timeoutSeconds)
            return input
        end run

        on doWithTimeout(uiScript, timeoutSeconds)
            set endDate to (current date) + timeoutSeconds
            repeat
                try
                    run script "tell application \\"System Events\\"
        " & uiScript & "
        end tell"
                    exit repeat
                on error errorMessage
                    if ((current date) > endDate) then
                        error "Can not " & uiScript
                    end if
                end try
            end repeat
        end doWithTimeout'''
    args = ['', '']

    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)
    if p.returncode == 0:
        return p.returncode
    else:
        raise Exception(stderr)


def launch_app(appname, delay=0.125):
    scpt = '''
        on run {input, parameters}
            (* Your script goes here *)
            delay ''' + str(delay) + '''
            tell application "''' + appname + '''" to activate
            return input
        end run'''
    args = ['', '']

    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)
    if p.returncode == 0:
        return p.returncode
    else:
        raise Exception(stderr)


def press_key(code, delay=0.125):
    scpt = '''
        on run {input, parameters}
            delay ''' + str(delay) + '''
            set timeoutSeconds to 2.0
            set uiScript to "key code ''' + str(code) + '''"
            my doWithTimeout(uiScript, timeoutSeconds)
            return input
        end run

        on doWithTimeout(uiScript, timeoutSeconds)
            set endDate to (current date) + timeoutSeconds
            repeat
                try
                    run script "tell application \\"System Events\\"
        " & uiScript & "
        end tell"
                    exit repeat
                on error errorMessage
                    if ((current date) > endDate) then
                        error "Can not " & uiScript
                    end if
                end try
            end repeat
        end doWithTimeout'''
    args = ['', '']

    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt)
    if p.returncode == 0:
        return p.returncode
    else:
        raise Exception(stderr)


def press_combination(code, keys, delay=0.125):
    if len(keys) > 3:
        raise Exception("Cannot Pass more than 3 keys in combination")
    else:
        flag = len(set(keys)) == len(keys)
        if not flag:
            raise Exception("Cannot Pass one key more than once")
        keys_dict = []
        for item in keys:
            if item == COMMON_KEYS.COMMAND or item == CONTROL_KEYS.OPTION or item == COMMON_KEYS.LSHIFT or item == COMMON_KEYS.RSHIFT:
                if item == COMMON_KEYS.COMMAND:
                    keys_dict.append("command down")
                if item == COMMON_KEYS.CONTROL:
                    keys_dict.append("control down")
                if item == COMMON_KEYS.LSHIFT or item == COMMON_KEYS.RSHIFT:
                    keys_dict.append("shift down")
            else:
                raise Exception("Invalid Input in 2nd argument")

        keys_string = '{'
        for item in keys_dict:
            keys_string += str(item)
            keys_string += ", "
        keys_string = keys_string[:-2]
        keys_string += '}'
        scpt = '''
                on run {input, parameters}
                    delay ''' + str(delay) + '''
                    set timeoutSeconds to 2.0
                    set uiScript to "key code \\"''' + str(code) + '''\\" using ''' + str(keys_string) + '''"
                    my doWithTimeout(uiScript, timeoutSeconds)
                    return input
                end run

                on doWithTimeout(uiScript, timeoutSeconds)
                    set endDate to (current date) + timeoutSeconds
                    repeat
                        try
                            run script "tell application \\"System Events\\"
                " & uiScript & "
                end tell"
                            exit repeat
                        on error errorMessage
                            if ((current date) > endDate) then
                                error "Can not " & uiScript
                            end if
                        end try
                    end repeat
                end doWithTimeout'''
        args = ['', '']

        p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
        stdout, stderr = p.communicate(scpt)
        if p.returncode == 0:
            return p.returncode
        else:
            raise Exception(stderr)
