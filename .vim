let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/code/time_tracking_via_gcal
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +23 pyproject.toml
badd +1 migrations/env.py
badd +29 time_tracking_via_gcal/models/user.py
badd +4 time_tracking_via_gcal/models/__init__.py
badd +5 migrations/env.py
badd +395 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/ext/declarative/api.py
badd +0 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/alembic/__init__.py
badd +4 .env
badd +1 time_tracking_via_gcal/models/base.py
badd +699 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/sql/sqltypes.py
badd +25 migrations/versions/1924a11946f8_init.py
badd +2 README.md
badd +1 time_tracking_via_gcal/db.py
badd +17 time_tracking_via_gcal/app.py
badd +1 time_tracking_via_gcal/bot.py
badd +221 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiopg/sa/engine.py
badd +179 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiopg/pool.py
badd +9 time_tracking_via_gcal/settings.py
badd +0 time_tracking_via_gcal/handlers/__init__.py
badd +1235 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/sql/schema.py
badd +163 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/aiopg/utils.py
badd +637 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/sql/selectable.py
badd +16 docker-compose.yml
badd +0 time_tracking_via_gcal/handlers/settings.py
badd +326 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/sql/elements.py
argglobal
silent! argdel *
edit time_tracking_via_gcal/bot.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
1wincmd h
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 96 + 96) / 193)
exe 'vert 2resize ' . ((&columns * 96 + 96) / 193)
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
45
normal! zo
let s:l = 106 - ((47 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
106
normal! 013|
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
let s:l = 31 - ((30 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
31
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 96 + 96) / 193)
exe 'vert 2resize ' . ((&columns * 96 + 96) / 193)
tabedit time_tracking_via_gcal/handlers/settings.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 64 + 96) / 193)
exe 'vert 2resize ' . ((&columns * 64 + 96) / 193)
exe 'vert 3resize ' . ((&columns * 63 + 96) / 193)
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 44 - ((43 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
44
normal! 05|
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
let s:l = 15 - ((14 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
15
normal! 040|
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
let s:l = 74 - ((27 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
74
normal! 0
wincmd w
2wincmd w
exe 'vert 1resize ' . ((&columns * 64 + 96) / 193)
exe 'vert 2resize ' . ((&columns * 64 + 96) / 193)
exe 'vert 3resize ' . ((&columns * 63 + 96) / 193)
tabedit time_tracking_via_gcal/models/user.py
set splitbelow splitright
wincmd _ | wincmd |
vsplit
wincmd _ | wincmd |
vsplit
2wincmd h
wincmd w
wincmd _ | wincmd |
split
1wincmd k
wincmd w
wincmd w
set nosplitbelow
set nosplitright
wincmd t
set winminheight=1 winminwidth=1 winheight=1 winwidth=1
exe 'vert 1resize ' . ((&columns * 64 + 96) / 193)
exe '2resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 2resize ' . ((&columns * 64 + 96) / 193)
exe '3resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 3resize ' . ((&columns * 64 + 96) / 193)
exe 'vert 4resize ' . ((&columns * 63 + 96) / 193)
argglobal
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 35 - ((34 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
35
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/models/base.py') | buffer time_tracking_via_gcal/models/base.py | else | edit time_tracking_via_gcal/models/base.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 5 - ((4 * winheight(0) + 15) / 31)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
5
normal! 08|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/models/__init__.py') | buffer time_tracking_via_gcal/models/__init__.py | else | edit time_tracking_via_gcal/models/__init__.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 4 - ((1 * winheight(0) + 15) / 31)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
4
normal! 0
wincmd w
argglobal
if bufexists('migrations/env.py') | buffer migrations/env.py | else | edit migrations/env.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 10 - ((9 * winheight(0) + 31) / 63)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
10
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 64 + 96) / 193)
exe '2resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 2resize ' . ((&columns * 64 + 96) / 193)
exe '3resize ' . ((&lines * 31 + 33) / 66)
exe 'vert 3resize ' . ((&columns * 64 + 96) / 193)
exe 'vert 4resize ' . ((&columns * 63 + 96) / 193)
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
