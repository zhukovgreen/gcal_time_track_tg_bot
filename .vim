let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/code/time_tracking_via_gcal
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 time_tracking_via_gcal/bot.py
badd +1 time_tracking_via_gcal/settings.py
badd +7 time_tracking_via_gcal/handlers/settings.py
badd +4 .env
badd +32 docker-compose.yml
badd +1 pip-wheel-metadata/time_tracking_via_gcal-0.1.0.dist-info/WHEEL
badd +1 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiogram/__init__.py
badd +1 time_tracking_via_gcal/models/user.py
badd +12 time_tracking_via_gcal/models/user_settings.py
badd +1 time_tracking_via_gcal/models/__init__.py
badd +0 migrations/versions/55d9bb11f1dd_init.py
badd +10 time_tracking_via_gcal/handlers/__init__.py
badd +17 time_tracking_via_gcal/handlers/reports.py
badd +72 time_tracking_via_gcal/handlers/service.py
badd +32 time_tracking_via_gcal/handlers/utils/data_processing.py
badd +1 time_tracking_via_gcal/models/dal.py
argglobal
silent! argdel *
edit time_tracking_via_gcal/models/dal.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
4wincmd h
wincmd w
wincmd w
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 31 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 28 + 120) / 240)
exe 'vert 3resize ' . ((&columns * 59 + 120) / 240)
exe '4resize ' . ((&lines * 29 + 31) / 62)
exe 'vert 4resize ' . ((&columns * 59 + 120) / 240)
exe '5resize ' . ((&lines * 29 + 31) / 62)
exe 'vert 5resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 6resize ' . ((&columns * 59 + 120) / 240)
argglobal
enew
file NERD_tree_1
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal nofen
wincmd w
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 59 - ((56 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
59
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/handlers/utils/data_processing.py') | buffer time_tracking_via_gcal/handlers/utils/data_processing.py | else | edit time_tracking_via_gcal/handlers/utils/data_processing.py | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 48 - ((38 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
48
normal! 024|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/handlers/__init__.py') | buffer time_tracking_via_gcal/handlers/__init__.py | else | edit time_tracking_via_gcal/handlers/__init__.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 18 - ((17 * winheight(0) + 14) / 29)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
18
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
let s:l = 55 - ((6 * winheight(0) + 14) / 29)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
55
normal! 05|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/bot.py') | buffer time_tracking_via_gcal/bot.py | else | edit time_tracking_via_gcal/bot.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 112 - ((51 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
112
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 31 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 28 + 120) / 240)
exe 'vert 3resize ' . ((&columns * 59 + 120) / 240)
exe '4resize ' . ((&lines * 29 + 31) / 62)
exe 'vert 4resize ' . ((&columns * 59 + 120) / 240)
exe '5resize ' . ((&lines * 29 + 31) / 62)
exe 'vert 5resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 6resize ' . ((&columns * 59 + 120) / 240)
tabedit time_tracking_via_gcal/handlers/service.py
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
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 60 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 3resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 4resize ' . ((&columns * 59 + 120) / 240)
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 81 - ((51 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
81
normal! 05|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/models/dal.py') | buffer time_tracking_via_gcal/models/dal.py | else | edit time_tracking_via_gcal/models/dal.py | endif
setlocal fdm=manual
setlocal fde=0
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=0
setlocal fml=1
setlocal fdn=20
setlocal fen
silent! normal! zE
let s:l = 26 - ((25 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
26
normal! 013|
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
let s:l = 38 - ((0 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
38
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/handlers/reports.py') | buffer time_tracking_via_gcal/handlers/reports.py | else | edit time_tracking_via_gcal/handlers/reports.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 34 - ((24 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
34
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 60 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 3resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 4resize ' . ((&columns * 59 + 120) / 240)
tabedit time_tracking_via_gcal/models/user_settings.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=0
set winheight=1
set winminwidth=0
set winwidth=1
exe 'vert 1resize ' . ((&columns * 120 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 119 + 120) / 240)
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 13 - ((12 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
13
normal! 09|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/models/user.py') | buffer time_tracking_via_gcal/models/user.py | else | edit time_tracking_via_gcal/models/user.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 13 - ((12 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
13
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 120 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 119 + 120) / 240)
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
