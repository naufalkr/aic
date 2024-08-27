gameDevGraph = {
    'Game Mathematics': {
        'Linear Algebra': {'Vector': 1, 'Matrix': 1},
        'Vector': {'Matrix': 1, 'Geometry': 1},
        'Matrix': {'Linear Transformation': 1, 'Geometry': 1},
        'Geometry': {'Affine Space': 1},
        'Affine Space': {'Affine Transformation': 1},
        'Affine Transformation': {'Orientation': 1},
        'Orientation': {'Quaternion': 1},
        'Quaternion': {'Curve': 1},
        'Curve': {'Spline': 1},
        'Spline': {'Euler Angle': 1},
        'Euler Angle': {'Hermite': 1},
        'Hermite': {'Bezier': 1},
        'Bezier': {'Catmull-Rom': 1},
        'Catmull-Rom': {'Projection': 1},
        'Projection': {'Perspective': 1, 'Orthogonal': 1},
        'Perspective': {},
        'Orthogonal': {},
    },
    
    'Game Physics Dynamics': {
        'Linear Velocity': {'Angular Velocity': 1},
        'Angular Velocity': {'Buoyancy': 1},
        'Buoyancy': {'Friction': 1},
        'Friction': {'Collision Detection CCD': 1},
        'Collision Detection CCD': {'Narrow Phase': 1, 'Broad Phase': 1},
        'Narrow Phase': {'SAT': 1, 'EPA': 1},
        'Broad Phase': {'GJK': 1, 'Intersection': 1},
        'SAT': {},
        'EPA': {},
        'GJK': {},
        'Intersection': {},
    },
    
    'Game Engine': {
        'Unreal Engine': {},
        'Unity 3D': {},
        'Godot': {},
        'Native': {},
    },
    
    'Programming Languages': {
        'C / C++': {},
        'C#': {},
        'Rust': {},
        'Python': {},
        'Assembly': {},
    },
    
    'Computer Graphics': {
        'Ray Tracing': {'Rasterization': 1},
        'Rasterization': {'Graphics Pipeline': 1},
        'Graphics Pipeline': {'Shader': 1},
        'Shader': {'Sampling': 1, 'Rendering Equation': 1},
        'Rendering Equation': {'Reflection Mapping': 1},
        'Reflection Mapping': {'Diffuse': 1, 'Specular': 1},
        'Diffuse': {'Texture': 1},
        'Specular': {'Texture': 1},
        'Texture': {'Bump': 1, 'Parallax': 1},
        'Bump': {'Horizon': 1},
        'Parallax': {'Horizon': 1},
        'Horizon': {},
    },
    
    'Graphics API': {
        'DirectX': {},
        'OpenGL': {},
        'Vulkan': {},
        'WebGL': {},
        'OpenGL ES': {},
        'Metal': {},
    },
    
    'Game AI': {
        'Decision Making': {'Movement': 1, 'Board Game': 1},
        'Movement': {},
        'Board Game': {},
        'Learning': {'Reinforcement Learning': 1},
        'Reinforcement Learning': {'Artificial Neural Network': 1},
        'Artificial Neural Network': {'Deep Learning': 1},
        'Deep Learning': {'Decision Tree Learning': 1},
        'Decision Tree Learning': {'Naive Bayes Classifier': 1},
        'Naive Bayes Classifier': {},
    },
    
    'Advanced Rendering': {
        'Real-Time Ray Tracing': {'DirectX Ray Tracing': 1, 'Vulkan Ray Tracing': 1},
        'DirectX Ray Tracing': {'OptiX': 1},
        'Vulkan Ray Tracing': {'OptiX': 1},
        'OptiX': {'Physically-Based Rendering': 1},
        'Physically-Based Rendering': {'Translucency and Transparency': 1},
        'Translucency and Transparency': {'Conservation of Energy': 1},
        'Conservation of Energy': {'Metallicity': 1},
        'Metallicity': {'Microsurface Scattering': 1},
        'Microsurface Scattering': {},
    },
}
