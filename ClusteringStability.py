import open3d as o3d

def test_quadric_decimation():
    # Create a test mesh (e.g., a sphere)
    mesh = o3d.geometry.TriangleMesh.create_sphere(radius=1.0)

    # Simplify using quadric decimation
    target_triangles = 8000  # Adjust this number as needed
    simplified_mesh_qd = mesh.simplify_quadric_decimation(target_number_of_triangles=target_triangles)

    # Visualize the original and simplified meshes
    print(f"Original triangles: {len(mesh.triangles)}")
    print(f"Simplified triangles: {len(simplified_mesh_qd.triangles)}")

    # Visualize the results
    o3d.visualization.draw_geometries([simplified_mesh_qd], window_name='Simplified Mesh')

    # Add assertions or checks for expected properties
    assert len(simplified_mesh_qd.triangles) <= target_triangles, "Triangle count exceeds target"

test_quadric_decimation()