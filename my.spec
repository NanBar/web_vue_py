# myapp.spec
# -*- mode: python -*-


block_cipher = None



# Analysis部分用于分析应用程序的依赖
a = Analysis(['main.py'],  # 应用程序的主脚本
             pathex=['.'],  # 应用程序路径
             binaries=[],  # 需要包含的二进制文件
             datas=[('templates', 'templates')],  # 包含 HTML 模板
             hiddenimports=['flask', 'flask_socketio', 'eventlet', 'serial',
                            # 这部分是必须手动指明的
                            'engineio.async_eventlet','eventlet.hubs.epolls','eventlet.hubs.kqueue','eventlet.hubs.selects','dns','dns.dnssec','dns.e164','dns.edns','dns.entropy','dns.exception','dns.flags','dns.grange','dns.hash','dns.inet','dns.ipv4','dns.ipv6','dns.message','dns.name','dns.namedict','dns.versioned','dns.node','dns.opcode','dns.query','dns.rcode','dns.rdata','dns.rdataclass','dns.rdataset','dns.rdatatype','dns.renderer','dns.resolver','dns.reversename','dns.rrset','dns.set','dns.tokenizer','dns.tsig','dns.tsigkeyring','dns.ttl','dns.update','dns.version','dns.wiredata','dns.zone','av','fvcore','torch','torchvision','detectron2',
                            ],  # 隐式导入的模块
             hookspath=[],  # 自定义hook路径
             hooksconfig={},  # hooks配置
             runtime_hooks=[],  # 运行时hook
             excludes=[],  # 排除的模块
             win_no_prefer_redirects=False,  # Windows下是否优先使用重定向
             win_private_assemblies=False,  # 是否使用私有程序集
             cipher=block_cipher,  # 数据加密
             noarchive=False)  # 是否不打包成zip文件

# PYZ部分用于打包Python字节码
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

# EXE部分用于定义可执行文件的设置
exe = EXE(pyz,
          a.scripts,  # 指定需打包的脚本
          [],
          exclude_binaries=True,  # 不打包二进制文件
          name='myapp',  # 应用程序名称
          debug=False,  # 是否启用调试模式
          bootloader_ignore_signals=False,  # 处理信号
          strip=False,  # 是否去除调试信息
          upx=True,  # 是否使用UPX压缩
          console=False)  # 是否使用控制台窗口

# COLLECT部分用于收集所有依赖项
coll = COLLECT(exe,
               a.binaries,  # 收集的二进制文件
               a.zipfiles,  # 收集的zip文件
               a.datas,  # 收集的数据文件
               strip=False,  # 是否去除调试信息
               upx=True,  # 是否使用UPX压缩
               upx_exclude=[],  # 不压缩的文件
               name='myapp')  # 最终应用程序名称
