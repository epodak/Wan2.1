import pkg_resources
import sys
from pkg_resources import DistributionNotFound, VersionConflict

def check_requirements():
    # 读取 requirements.txt
    requirements = []
    with open('requirements.txt') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                requirements.append(line)

    # 检查每个包的版本
    missing = []
    mismatch = []
    ok = []

    for requirement in requirements:
        try:
            pkg_resources.require(requirement)
            ok.append(requirement)
        except DistributionNotFound as e:
            missing.append(requirement)
        except VersionConflict as e:
            installed = e.dist
            required = e.req
            mismatch.append((requirement, str(installed)))

    # 输出结果
    print("\n=== 环境检查结果 ===")

    if ok:
        print("\n✅ 已正确安装的包:")
        for pkg in ok:
            print(f"  - {pkg}")

    if mismatch:
        print("\n⚠️ 版本不匹配的包:")
        for req, inst in mismatch:
            print(f"  - 需要: {req}")
            print(f"    已安装: {inst}")

    if missing:
        print("\n❌ 未安装的包:")
        for pkg in missing:
            print(f"  - {pkg}")

    return len(missing) == 0 and len(mismatch) == 0

if __name__ == "__main__":
    print(f"Python 版本: {sys.version}")
    if check_requirements():
        print("\n✨ 所有依赖包都已正确安装！")
    else:
        print("\n⚠️ 建议创建新的虚拟环境并安装所需依赖")
        print("创建新环境的步骤：")
        print("conda create -n wan21 python=3.10")
        print("conda activate wan21")
        print("pip install -r requirements.txt")
