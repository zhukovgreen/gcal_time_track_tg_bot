let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/code/time_tracking_via_gcal
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 token.pickle
badd +14 tests/test_basic.py
badd +1 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/googleapiclient/discovery.py
badd +407 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/google_auth_oauthlib/flow.py
badd +21 time_tracking_via_gcal/app.py
badd +7 tests/test_integration.py
badd +11 tests/conftest.py
badd +1 time_tracking_via_gcal/__main__.py
badd +24 time_tracking_via_gcal/bot.py
badd +82 time_tracking_via_gcal/handlers/__init__.py
badd +1 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/utils/__init__.py
badd +851 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/dispatcher/dispatcher.py
badd +126 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/utils/executor.py
badd +11 time_tracking_via_gcal/settings.py
badd +419 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiohttp/web.py
badd +280 /usr/lib/python3.7/asyncio/events.py
badd +133 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiohttp/web_app.py
badd +1 tests/__init__.py
badd +69 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aresponses/main.py
badd +13 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/types/reply_keyboard.py
badd +27 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/dispatcher/handler.py
badd +32 time_tracking_via_gcal/handlers/data_processing.py
badd +395 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/types/message.py
badd +18 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/types/base.py
badd +18 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/types/input_file.py
badd +19 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiofiles/threadpool/__init__.py
badd +28 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/types/__init__.py
badd +101 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/pandas/core/generic.py
badd +21 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/types/file.py
badd +205 /usr/lib/python3.7/concurrent/futures/thread.py
badd +1 time_tracking_via_gcal/gcal_manager.py
badd +2 time_tracking_via_gcal/utils.py
badd +182 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/google/auth/transport/requests.py
badd +499 /usr/lib/python3.7/shutil.py
badd +3 time_tracking_via_gcal/handlers/settings.py
badd +273 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/dispatcher/storage.py
badd +7 docker-compose.yml
badd +23 Dockerfile
badd +1 .env
badd +151 .dockerignore
argglobal
silent! argdel *
edit time_tracking_via_gcal/handlers/data_processing.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
3wincmd h
wincmd w
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 2resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 3resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 4resize ' . ((&columns * 67 + 137) / 274)
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 32 - ((31 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
32
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/gcal_manager.py') | buffer time_tracking_via_gcal/gcal_manager.py | else | edit time_tracking_via_gcal/gcal_manager.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 75 - ((47 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
75
normal! 011|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/bot.py') | buffer time_tracking_via_gcal/bot.py | else | edit time_tracking_via_gcal/bot.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=3
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 58 - ((31 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
58
normal! 038|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/handlers/__init__.py') | buffer time_tracking_via_gcal/handlers/__init__.py | else | edit time_tracking_via_gcal/handlers/__init__.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=3
setlocal fml=1
setlocal fdn=20
setlocal fen
64
normal! zo
let s:l = 101 - ((55 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
101
normal! 020|
wincmd w
exe 'vert 1resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 2resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 3resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 4resize ' . ((&columns * 67 + 137) / 274)
tabedit .env
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
3wincmd h
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd w
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe '1resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 1resize ' . ((&columns * 68 + 137) / 274)
exe '2resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 2resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 3resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 4resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 5resize ' . ((&columns * 67 + 137) / 274)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 3 - ((2 * winheight(0) + 15) / 31)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
3
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/settings.py') | buffer time_tracking_via_gcal/settings.py | else | edit time_tracking_via_gcal/settings.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 4 - ((3 * winheight(0) + 15) / 31)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
4
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/app.py') | buffer time_tracking_via_gcal/app.py | else | edit time_tracking_via_gcal/app.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 14 - ((13 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
14
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/bot.py') | buffer time_tracking_via_gcal/bot.py | else | edit time_tracking_via_gcal/bot.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=3
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 25 - ((24 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
25
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/handlers/settings.py') | buffer time_tracking_via_gcal/handlers/settings.py | else | edit time_tracking_via_gcal/handlers/settings.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 6 - ((5 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
6
normal! 010|
wincmd w
2wincmd w
exe '1resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 1resize ' . ((&columns * 68 + 137) / 274)
exe '2resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 2resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 3resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 4resize ' . ((&columns * 68 + 137) / 274)
exe 'vert 5resize ' . ((&columns * 67 + 137) / 274)
tabedit docker-compose.yml
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 137 + 137) / 274)
exe 'vert 2resize ' . ((&columns * 136 + 137) / 274)
argglobal
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 3 - ((2 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
3
normal! 05|
wincmd w
argglobal
if bufexists('Dockerfile') | buffer Dockerfile | else | edit Dockerfile | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 19 - ((18 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
19
normal! 08|
wincmd w
exe 'vert 1resize ' . ((&columns * 137 + 137) / 274)
exe 'vert 2resize ' . ((&columns * 136 + 137) / 274)
tabnext 2
if exists('s:wipebuf') && getbufvar(s:wipebuf, '&buftype') isnot# 'terminal'
  silent exe 'bwipe ' . s:wipebuf
endif
unlet! s:wipebuf
set winheight=1 winwidth=20 winminheight=1 winminwidth=1 shortmess=filnxtToOF
let s:sx = expand("<sfile>:p:r")."x.vim"
if file_readable(s:sx)
  exe "source " . fnameescape(s:sx)
endif
let &so = s:so_save | let &siso = s:siso_save
doautoall SessionLoadPost
unlet SessionLoad
" vim: set ft=vim :
