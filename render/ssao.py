"""第 55 批：墙角 AO 一圈一圈、角色和地面接触处黑圈、远处..."""

def world_radius(radius, scale):
    """把屏幕半径换算为世界半径。"""
    raise NotImplementedError("TODO: world_radius")

def bilateral_depth(center_depth, neighbor_depth):
    """返回深度双边上采样权重。"""
    raise NotImplementedError("TODO: bilateral_depth")

def encode_normal(nx, ny, nz):
    """返回八面体法线编码。"""
    raise NotImplementedError("TODO: encode_normal")

def sample_count(radius, quality):
    """按半径返回自适应采样数。"""
    raise NotImplementedError("TODO: sample_count")

def world_noise(uv, frame):
    """返回世界坐标噪点。"""
    raise NotImplementedError("TODO: world_noise")

def dedupe_ao(direct, ao):
    """避免 AO 与直接光重复乘。"""
    raise NotImplementedError("TODO: dedupe_ao")

def transparent_ao(alpha):
    """判断透明像素是否排除 AO。"""
    raise NotImplementedError("TODO: transparent_ao")

def upsample_ao(center_depth, neighbor_depth):
    """返回深度感知 AO 上采样权重。"""
    raise NotImplementedError("TODO: upsample_ao")

def reset_history(camera_changed):
    """相机切换时重置 AO 历史。"""
    raise NotImplementedError("TODO: reset_history")

def apply_before_fog(ao, fog):
    """在雾前应用 AO。"""
    raise NotImplementedError("TODO: apply_before_fog")
