let SessionLoad = 1
let s:so_save = &so | let s:siso_save = &siso | set so=0 siso=0
let v:this_session=expand("<sfile>:p")
silent only
cd ~/Dropbox/code/time_tracking_via_gcal
if expand('%') == '' && !&modified && line('$') <= 1 && getline(1) == ''
  let s:wipebuf = bufnr('%')
endif
set shortmess=aoO
badd +1 .gitignore
badd +24 time_tracking_via_gcal/bot.py
badd +124 time_tracking_via_gcal/handlers/service.py
badd +142 time_tracking_via_gcal/models/dal.py
badd +65 time_tracking_via_gcal/utils/gcal_manager.py
badd +179 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/googleapiclient/discovery.py
badd +6 .env
badd +265 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/google_auth_oauthlib/flow.py
badd +6 tests/test_gcal_connection.py
badd +1923 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/oauth2client/client.py
badd +106 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/google/oauth2/service_account.py
badd +49 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/google/auth/_service_account_info.py
badd +28 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/google/auth/__init__.py
badd +19 time_tracking_via_gcal/handlers/reports.py
badd +1 credentials.json
badd +5 secrets.json
badd +18 time_tracking_via_gcal/models/user.py
badd +6 time_tracking_via_gcal/structs.py
badd +59 time_tracking_via_gcal/handlers/settings.py
badd +170 ~/.pyenv/versions/3.7-dev/lib/python3.7/re.py
badd +1 time_tracking_via_gcal/handlers/__init__.py
badd +1 NERD_tree_3
badd +2713 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/sql/sqltypes.py
badd +1079 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/dialects/postgresql/base.py
badd +21 migrations/versions/80726396cd81_init.py
badd +19 migrations/versions/c22ee0047eed_init.py
badd +28 migrations/versions/3505efd09bb2_init.py
badd +231 ~/.cache/pypoetry/virtualenvs/time-tracking-via-gcal-f98ImiSB-py3.7/lib/python3.7/site-packages/sqlalchemy/util/_collections.py
badd +1 migrations/env.py
badd +4 time_tracking_via_gcal/models/__init__.py
badd +1 time_tracking_via_gcal/models/report_settings.py
argglobal
silent! argdel *
edit time_tracking_via_gcal/bot.py
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
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
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
27
normal! zo
let s:l = 61 - ((33 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
61
normal! 018|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/models/dal.py') | buffer time_tracking_via_gcal/models/dal.py | else | edit time_tracking_via_gcal/models/dal.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 91 - ((26 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
91
normal! 04|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/handlers/service.py') | buffer time_tracking_via_gcal/handlers/service.py | else | edit time_tracking_via_gcal/handlers/service.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 123 - ((35 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
123
normal! 05|
wincmd w
exe 'vert 1resize ' . ((&columns * 60 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 3resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 4resize ' . ((&columns * 59 + 120) / 240)
tabedit time_tracking_via_gcal/models/dal.py
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
let s:l = 11 - ((10 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
11
normal! 017|
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/handlers/service.py') | buffer time_tracking_via_gcal/handlers/service.py | else | edit time_tracking_via_gcal/handlers/service.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 92 - ((30 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
92
normal! 05|
wincmd w
exe 'vert 1resize ' . ((&columns * 120 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 119 + 120) / 240)
tabedit migrations/env.py
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
setlocal fdl=2
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 1 - ((0 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
1
normal! 0
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
let s:l = 15 - ((14 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
15
normal! 05|
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
let s:l = 7 - ((6 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
7
normal! 0
wincmd w
argglobal
if bufexists('time_tracking_via_gcal/models/report_settings.py') | buffer time_tracking_via_gcal/models/report_settings.py | else | edit time_tracking_via_gcal/models/report_settings.py | endif
setlocal fdm=expr
setlocal fde=SimpylFold#FoldExpr(v:lnum)
setlocal fmr={{{,}}}
setlocal fdi=#
setlocal fdl=1
setlocal fml=1
setlocal fdn=20
setlocal fen
let s:l = 4 - ((3 * winheight(0) + 29) / 59)
if s:l < 1 | let s:l = 1 | endif
exe s:l
normal! zt
4
normal! 0
wincmd w
exe 'vert 1resize ' . ((&columns * 60 + 120) / 240)
exe 'vert 2resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 3resize ' . ((&columns * 59 + 120) / 240)
exe 'vert 4resize ' . ((&columns * 59 + 120) / 240)
tabnext 1
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
